# We have a special line (**Interrupt Request Line**) connecting I/O to the Processor’s [[FSMs]].

- We have special code that handles these Interrupt Requests.

## Note the following:

- We must have a dedicated address to go to when we wish to handle interrupt requests. This is where we put our IRH, `0x20` on NOIS II.
- We must return to our original position (address) in the program. We have a specific address, ea, exception address that stores this last position..
- Important states i.e. register values must be stored on the stack and restored before returning from the interrupt.
- Must enable [[Interrupts]] on the processor.
- Must enable interrupts to be allocated for the processor, we ask the question: what action triggers an interrupt?