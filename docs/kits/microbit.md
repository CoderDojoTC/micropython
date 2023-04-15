# MicroBit

Although the BBC MicroBit is a good educational product for learning MicroPython, we don't use it in our MicroPython courses for the following reason:


1. **Price** - The current price on sites like Amazon is around $22.  We can get the Raspberry Pi Pico for $4.
2. **Availability** - MicroBits have not been available due to shortages of chips that it needs.
3. **Memory** - The MicroBit only has 32KB of RAM.  The Pico has 256K.  We need this extra RAM for our OLED display labs.
4. **Breadboard** - We use simple, standardized, easy-to-upgrade breadboards in our classes.  This makes it easy to upgrade our microcontrollers and promotes higher sustainability.  We also believe that teaching breadboarding skills is critical for future projects.
5. **Expandability** - we like the ability to expand our base labs to include many low costs sensors
6. **Multi-Core** - we want to be able to teach multi-core coding in our classrooms.  Because the MicroBit only has a single core this is not possible on the MicroBit.  The Raspberry Pi Pico has two cores.  Many projects use one core for monitoring the sensors and another core for doing analysis and updating the display.
7. **Pulse Width Modulation Channels** - The MicroBit only has 3 PWM channels.  We need a minimum of 4 to drive our robots.

## Side-By-Side Comparision

|Feature Name|MicroBit v2|Raspberry Pi Pico|Notes|
|-----|---|---|-------|
|Price|$22|$4|The Pico "W" with wireless is $6|
|Breadboard|No|Yes|Allows us to teach breadboarding skills|
|RAM|32MB|256MB|We need around 100MB to support our 128x64 OLED frame buffers|
|Flash|2MB|512MB|We use extra flash to store hundreds of programs, images and sounds|
|Sensors|Temp,Accelerometers,Compass,Light,Touch|Temp|For about $5 we can add these sensors to the Pico|
|Processor|ARM Cortex-M4|Dual-core Arm Cortex-M0+|The M4 has better support for DSP and floating point|
|LEDs|25|1|We use 8X8 LEDs and NeoPixels in our labs to create similar displays|
|Block Programming|Microsoft MakeCode|BIPES|Block coding is great for younger students that don't have strong keyboarding skills|
|GPIOs|20|26|This has not been a concern.  None of our labs need over 20 GPIOs|
|ADCs|5|3|Also not a concern.  None of our labs need more that 3 Analog to Digital converters that run concurrently|
|Serial Bus|1 I2C, 1 SPI|2x UART, 2x I2C, 2x SPI, up to 16 PWM channels|
|Pulse Width Modulation|3|16|We need 4 PWM to drive our robots (a forward and back for each motor)|


## Sample Sources

## Microcenter

* [MicroCenter MicroBit Go Bundle for $22.92](https://www.microcenter.com/product/648994/microbit-v2-go-bundle) - includes USB cable and battery pack

## SparkFun

* [Pico for $3.99](https://www.sparkfun.com/products/17829)
* [Microbit for $22](https://www.sparkfun.com/products/17287)
* [Breakout Board for Breadboards $7](https://www.sparkfun.com/products/16446)

## References

* [Cytron](https://www.cytron.io/tutorial/raspberry-pico-vs-microbit)
* [Pico:ed V2 - a RP2040 in MicroBit Form Factor](https://www.cnx-software.com/2022/09/28/raspberry-pi-rp2040-gets-into-bbc-microbit-lookalike-board/)
* [Pico:ed $12](https://www.elecfreaks.com/elecfreaks-pico-ed-v2.html)