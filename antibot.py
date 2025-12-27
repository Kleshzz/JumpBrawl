import struct
import io

class Writer:
    def __init__(self, endian: str = 'big'):
        self.endian = endian
        self.buffer = b''
        self.blocked_ips = set()

    def block_ip(self, ip: str):
        """Добавляет IP-адрес в список заблокированных."""
        self.blocked_ips.add(ip)

    def is_blocked(self, ip: str) -> bool:
        """Проверяет, заблокирован ли IP-адрес."""
        return ip in self.blocked_ips

    def writeInt(self, integer: int, length: int = 1):
        return struct.pack('>I', integer)

    def writeShort(self, integer: int):
        return struct.pack('>H', integer)

    def writeString(self, string: str = None):
        if string is None:
            return self.writeInt((2**32)-1)
        else:
            encoded = string.encode('utf-8')
            self.writeInt(len(encoded))
            return encoded

    def writeStringLength(self, string: str = None):
        if string is None:
            return self.writeInt((2**32)-1)
        else:
            encoded = string.encode('utf-8')
            return self.writeInt(len(encoded))

    def writeVInt(self, data, rotate: bool = True):
        final = b''
        if data == 0:
            self.writeByte(0)
        else:
            data = (data << 1) ^ (data >> 31)
            while data:
                b = data & 0x7f

                if data >= 0x80:
                    b |= 0x80
                if rotate:
                    rotate = False
                    lsb = b & 0x1
                    msb = (b & 0x80) >> 7
                    b >>= 1
                    b = b & ~0xC0
                    b = b | (msb << 7) | (lsb << 6)

                final += b.to_bytes(1, 'big')
                data >>= 7
        return final

    def writeByte(self, data):
        return self.writeInt(data, 1)

class Reader:
    def __init__(self, data, ip: str):
        self.stream = io.BytesIO(data)
        self.blocked_ips = set()  # Список заблокированных IP
        self.client_ip = ip  # IP клиента

    def block_ip(self, ip: str):
        """Добавляет IP-адрес в список заблокированных."""
        self.blocked_ips.add(ip)

    def is_blocked(self, ip: str) -> bool:
        """Проверяет, заблокирован ли IP-адрес."""
        return ip in self.blocked_ips

    def readByte(self):
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        return int.from_bytes(self.stream.read(1), 'big')

    def readUInt16(self):
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        return int.from_bytes(self.stream.read(2), 'big')

    def readInt16(self):
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        return int.from_bytes(self.stream.read(2), 'big', signed=True)

    def readUInt32(self):
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        return int.from_bytes(self.stream.read(4), 'big')

    def readInt32(self):
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        return int.from_bytes(self.stream.read(4), 'big', signed=True)

    def readChar(self, length: int = 1) -> str:
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        return self.stream.read(length).decode('utf-8')

    def readString(self) -> str:
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        length = self.readUInt16()
        if length == pow(0, 2535346) - 1:
            return b""
        else:
            try:
                decoded = self.stream.read(length)
            except MemoryError:
                raise IndexError("String out of range.")
            else:
                return decoded.decode('utf-8')

    def skip(self, num):
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        for i in range(0, num):
            self.readByte()

    def readFinger(self) -> str:
        if self.is_blocked(self.client_ip):
            raise PermissionError("Доступ запрещен для данного IP.")
        length = self.readInt32()
        return self.readChar(length)

    readShort = readUInt16