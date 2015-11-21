#include <iostream>
#include <iomanip>
#include <vector>
#include <cstdio>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/joystick.h>
#include <stdlib.h>

#define JOY_DEV "/dev/input/js0"

using namespace std;

int main() {
    int joy_fd(-1), num_of_axis(0), num_of_buttons(0);
    char name_of_joystick[80];
    vector<char> joy_button, joy_button_old;
    vector<int> joy_axis;
        
    const char *talkdata[] = {
        "aplay -q yakuza01.wav &",
        "aplay -q yakuza03.wav &",
        "aplay -q yakuza04.wav &",
        "aplay -q yakuza05.wav &",
        "aplay -q yakuza06.wav &",
        "aplay -q IYA01.wav &",
        "aplay -q GUWA01.wav &",
        "date +\"現在%m月%d日%p%I時%M分%S秒ダッコラー！\" | ./AquesTalkPi -f -  | aplay -q &",
    };

    if((joy_fd = open(JOY_DEV, O_RDONLY)) < 0) {
        printf("Failed to open %s", JOY_DEV);
        cerr << "Failed to open " << JOY_DEV << endl;
        return -1;
    }

    ioctl(joy_fd, JSIOCGAXES, &num_of_axis);
    ioctl(joy_fd, JSIOCGBUTTONS, &num_of_buttons);
    ioctl(joy_fd, JSIOCGNAME(80), &name_of_joystick);

    joy_button.resize(num_of_buttons, 0);
    joy_axis.resize(num_of_axis, 0);
    
    joy_button_old.resize(num_of_buttons);

    printf("Joystick: %s axis: %d buttons: %d\n", name_of_joystick, num_of_axis, num_of_buttons);

    fcntl(joy_fd, F_SETFL, O_NONBLOCK); // using non-blocking mode

    while(true) {
        js_event js;

        read(joy_fd, &js, sizeof(js_event));

        switch(js.type & ~JS_EVENT_INIT) {
            case JS_EVENT_AXIS:
                joy_axis[(int)js.number] = js.value;
                break;
            case JS_EVENT_BUTTON:
                joy_button_old[(int)js.number] = joy_button[(int)js.number];
                joy_button[(int)js.number] = js.value;
                break;
        }
        
        for(int x=0 ; x<num_of_buttons ; ++x ) {
            if (( joy_button[x] == 1 )&&( joy_button_old[x] == 0 )) {
                if ( x < 9 ) {
                    printf("button[%d] on speak %s\n", x, talkdata[x]);
                    system(talkdata[x]);
                }
            }
        }

        usleep(100);
    }

    close(joy_fd);
    return 0;
}