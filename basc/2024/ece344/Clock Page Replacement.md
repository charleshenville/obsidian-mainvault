A method of [[Page Replacement]]

## DS
- Keeping cyclic list of pages in mem
- reference bit for each page in mem
- Iterator (hand) pointing to last element looked at

## A
- Check hand ref bit
	- if 0: place page, adv. hand
	- if 1: set to 0, adv. hand, repeat 
- set ref = 1 for accesses