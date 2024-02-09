# Hardware Timers

- Must have an accurate clock from [[Flip-Flops]] running at a specific frequency.
- Use a rate divider to correct the frequency to what we want.

## Interval Timer

|Address, Name|31→16|15→4|3|2|1|0|
|---|---|---|---|---|---|---|
|0xff202000 Status Register|-|-|-|-|R|Time Out Bit|
|0xff202004 Control Register|-|-|Stop|Start|CONT (Continuously count down over and over)|ITO|
|0xff202008 Start Value (L)|-|Counter Start Value (Low Order)|→|→|→|→|
|0xff20200c Start Value (H)|-|Counter Start Value (Higher Order)|→|→|→|→|

### Using this in software

1. Messily put the starting value into the two memory addresses. No good reason for doing it this way, unfortunately 😞.
2. Turn on START and CONT bits into control registers, this sets the timer running, ie loading the start value into the start value register in the hardware.
3. Poll the TO bit to determine when the counter has reached zero.
4. Store 0 into the bit 0 of the Status Register to reset its value.

`.equ` is an equate statement/directive.