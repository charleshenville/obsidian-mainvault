# Message Definition as A Guideline:

``` C

#include <stdint.h>

#define RADAR_DEVICE_ID 1
#define LIDAR_DEVICE_ID 2
#define CAM_DEVICE_ID   3
#define GPS_DEVICE_ID   4
#define IMU_DEVICE_ID   5
#define AUX_DEVICE_ID   6

/* Frame ids. */

#define AV_STATE_MSGID  0x11
#define AV_LIGHT_MSGID  0x11 // Need to get this MSG ID from the VI team
#define IMU_MSGID1      0x174
#define IMU_MSGID2      0x178

#define REQ_RADAR_MSGID         0x100
#define REQ_LIDAR_MSGID         0x101
#define REQ_CAM_MSGID           0x102
#define REQ_GPS_MSGID           0x103
#define REQ_IMU_MSGID           0x104
#define REQ_AUX_MSGID           0x105

#define ACK_RADAR_CHG_MSGID     0x106
#define ACK_LIDAR_CHG_MSGID     0x107
#define ACK_CAM_CHG_MSGID       0x108
#define ACK_GPS_CHG_MSGID       0x109
#define ACK_IMU_CHG_MSGID       0x110
#define ACK_AUX_CHG_MSGID       0x111

#define STA_RADAR_MSGID         0x112
#define STA_LIDAR_MSGID         0x113
#define STA_CAM_MSGID           0x114
#define STA_GPS_MSGID           0x115
#define STA_IMU_MSGID           0x116
#define STA_AUX_MSGID           0x117

#define LIDAR1_ISENSE_MSGID     0x120
#define LIDAR2_ISENSE_MSGID     0x121
#define LIDAR3_ISENSE_MSGID     0x122
#define LIDAR4_ISENSE_MSGID     0x123
#define LIDAR5_ISENSE_MSGID     0x124
#define CAM1_ISENSE_MSGID       0x125
#define CAM2_ISENSE_MSGID       0x126
#define CAM3_ISENSE_MSGID       0x127
#define CAM4_ISENSE_MSGID       0x128
#define RADAR1_ISENSE_MSGID     0x129
#define RADAR2_ISENSE_MSGID     0x12a
#define GPS_ISENSE_MSGID        0x12b
#define IMU_ISENSE_MSGID        0x12c
#define AUX1_ISENSE_MSGID       0x12d
#define AUX2_ISENSE_MSGID       0x12e

#define PWR_CHG_ERR             0x12f

typedef struct scoring_av_state_t {

    /**
     * Range: 0..3 (0..3 -)
     * Scale: 1
     * Offset: 0
     */

    uint8_t rolling_count;
    
    /**
     * Range: 0..2 (0..2 -)
     * Scale: 1
     * Offset: 0
     */

    uint8_t global_autonomy_status;
    
    /**
     * Range: 0..1 (0..1 -)
     * Scale: 1
     * Offset: 0
     */

    uint8_t steering_ctrl_active;

    /**
     * Range: 0..1 (0..1 -)
     * Scale: 1
     * Offset: 0
     */

    uint8_t friction_brake_ctrl_active;

    /**
     * Range: 0..1 (0..1 -)
     * Scale: 1
     * Offset: 0
     */

    uint8_t propulsion_ctrl_active;

} scoring_av_state_t;

typedef struct device_currents_t{
    uint32_t update_time;
    uint32_t radar1_i;
    uint32_t radar2_i;
    uint32_t lidar1_i;
    uint32_t lidar2_i;
    uint32_t lidar3_i;
    uint32_t lidar4_i;
    uint32_t lidar5_i;
    uint32_t gps_i;
    uint32_t imu_i;
    uint32_t cam1_i;
    uint32_t cam2_i;
    uint32_t cam3_i;
    uint32_t cam4_i;
    uint32_t aux1_i;
    uint32_t aux2_i;
} device_currents_t;

uint32_t isense_translate(int value);

```

`REQ` messages tell us **which devices to turn on**. 
- If you write `0x11` to `Byte0` and `0x11` to `Byte1` of those messages, the specified device will turn on. 
- To turn off the device, we write `0x00` to both bytes. For example, to turn on all radars, we write `msg.buf[0] = 0x11` and `msg.buf[1] = 0x11` to `msg.id = 0x100`.

`ACK` messages acknowledge that a **power state transition has been made** for a specific device group. 
- Before sending any more requests to the controller, always confirm that Electrical has published an ACK message to previous request

`STA` messages are published every 100ms and tell us what the **state of each device** is. 
- These are also published with an ACK message whenever the state of a device changes due to a request

`ISENSE` messages publish every 1s and tell us if the **devices are operating in the normal range**. 
- We should read these messages when they come in. If the first byte of the message is `0x00`, then the device is operating normally. 
- If the first byte is `0x0F`, then the device has a low-current error. If the first byte is `0xF0`, then the device has a high-current warning.

### NOTE: If we ever get a `PWR_CHG_ERR` with contents `0xFF`,  we should re-try sending the message.
