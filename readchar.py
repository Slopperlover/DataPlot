"""
Tiny module to read a single ASCII character, without needing to use Enter.

With system-defined implementations such as input() and sys.stdin.read(1), the
program halts until a newline is fed (most often by pressing the Enter key).
This behavior is suboptimal for some use cases.

This library removes the newline feeding step. The program continues after a
single ASCII value is entered.

Only `read_char()` and `read_byte()` should be used by end users.  No
arguments required.

------------------------------------------------------------------------------

This is a single-file version of module readchar's `readkey()` functionality
by Miguel Angel Garcia.  To accomplish this, code has been reorganized and
placed into different classes.  Documentation is updated, and functionality is
extended to support returning raw `bytes` objects as well as `str`.

See https://github.com/magmax/python-readchar for more information.

Both are based on a solution presented by Danny Yoo on ActiveState on
2002-06-21, and the discussion that followed. For that discussion, see
https://code.activestate.com/recipes/134892/

------------------------------------------------------------------------------

MIT Licence

Copyright (c) 2022, 2023 Miguel Angel Garcia, Patrick de Kok

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicence, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
class _ReadChar:
    """
    Gets a single character from standard input.  Does not echo to the screen.

    The exact implementation depends on the underlying operating system.
    """
    def __init__(self):
        """
        Selects the implementation based on operating system.

        OS-specific implementations will have imports that will raise
        ImportError when run with any other OS.
        """
        # Note: This is not where you would normally import modules.
        # In this case, I do this to hide `platform` from code that imports
        # the current module we're making.  There are other, multi-file ways
        # to do this neater.
        from sys import platform
        if platform.startswith(("linux", "darwin", "freebsd", "openbsd")):
            self.impl = _ReadCharUnix()
        elif platform in ("win32", "cygwin"):
            self.impl = _ReadCharWindows()
        else:
            raise NotImplementedError(f"The platform {platform} is not supported yet")

    def read_byte(self) -> bytes:
        """
        Reads a single character from input, and returns it as a byte.

        This block until a character is available.
        """
        return self.impl.read_byte()

    def read_char(self) -> str:
        """
        Reads a single character from input, and returns it as a str.

        This block until a character is available.
        """
        return self.impl.read_char()


class _ReadCharUnix:
    """
    Implementation for _ReadChar that is supported on POSIX systems.

    These include Unix, Linux, macOS and BSD distributions.
    """
    def __init__(self):
        try:
            import termios
        except ImportError:
            msg = f"_ReadCharUnix could not be used; termios is unavailable"
            raise NotImplementedError(msg)

    def _read(self, istream) -> str | bytes:
        """
        Helper function for read_char() and read_byte().
        """
        import sys
        import termios
    
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        term = termios.tcgetattr(fd)
        try:
            term[3] &= ~(termios.ICANON | termios.ECHO | termios.IGNBRK | termios.BRKINT)
            termios.tcsetattr(fd, termios.TCSAFLUSH, term)
    
            ch = istream.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def read_byte(self) -> bytes:
        import sys
        return self._read(sys.stdin.buffer)

    def read_char(self) -> str:
        import sys
        return self._read(sys.stdin)


class _ReadCharWindows:
    def __init__(self):
        try:
            import msvcrt
        except ImportError:
            msg = f"_ReadCharWindows could not be used; msvcrt is unavailable"
            raise NotImplementedError(msg)

    def read_byte(self) -> bytes:
        import msvcrt
        return msvcrt.getch()

    def read_char(self) -> str:
        # manual byte decoding because some bytes in windows are not utf-8 encodable.
        return chr(int.from_bytes(self.read_byte(), "big"))

__read_chars = _ReadChar()


def read_byte() -> bytes:
    """
    Reads a single character from input, and returns it as a byte.

    This block until a character is available.
    """
    return __read_chars.read_byte()

def read_char() -> str:
    """
    Reads a single character from input, and returns it as a string.

    This block until a character is available.
    """
    return __read_chars.read_char()


def __example_usage(bytes=False):
    """
    Example usage of this library.

    This function is not meant to be used as-is by end users, but its source
    code may inspire them how this module is to be used in their own code.
    """
    import sys
    print("Provide 1 character of input: ", end="")
    sys.stdout.flush()
    if bytes:
        c = read_byte()
        try:
            c_str = chr(int.from_bytes(c, "big"))
        except:
            c_str = c
    else:
        c = read_char()
        c_str = c
    t = type(c)

    print(f"""
Input: {c_str}
Type:  {t}
OS:    {sys.platform}""")


if __name__ == "__main__":
    __example_usage(bytes=True)
    print("\nNow do it all again!")
    __example_usage(bytes=False)
