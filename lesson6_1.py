import gpiozero as zero
import RPi.GPIO as GPIO
from time import sleep



if __name__ == "__main__":
    mcp3008_ch07 = zero.MCP3008(channel=7)
    mcp3008_ch06 = zero.MCP3008(channel=6)
    try:
        while True:
            value = round(mcp3008_ch07.value*100)
            print("光敏電處值: ", value)
            if value > 20:
                print("LIGHT")
            else:
                print("DARK")           

            requests.get(f'https://qooq12315-studious-space-tribble-6j9wv6445qj34rxq-8000.preview.app.github.dev/raspberry?Light={value}&temperature={mcp3008_ch6.value}')
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("程序退函数")