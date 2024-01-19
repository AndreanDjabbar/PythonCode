from data import subnet_mask, subnet_bit as subnet_bit_data
import math

class Ip:

    def __init__(self, ip):
        self.ip = ip
        self.__ip_class = None
        self.__subnet = None

        ip_break = ip.split('.')
        first_octet = int(ip_break[0])

        if (first_octet >= 0 and first_octet< 128):
            self.__ip_class = 'A'
        
        elif (first_octet >= 128 and first_octet < 192):
            self.__ip_class = 'B'

        elif (first_octet >= 192 and first_octet < 224):
            self.__ip_class = 'C'

        elif (first_octet >= 224 and first_octet < 240):
            self.__ip_class = 'D'
        
        elif (first_octet >= 240 and first_octet < 256):
            self.__ip_class = 'E'

    def set_subnet(self, input_subnet):
        subnet = subnet_mask.get(input_subnet)
        current_subnet = int(input_subnet[1:])
        default_bit = [0, 0, 0, 0]
        active_bit = math.floor(current_subnet / 8)
        inactive_bit = current_subnet % 8
        current_index = 0

        if active_bit > 0:
            for a in range(active_bit):
                default_bit[a] = 255
                current_index += 1

        if inactive_bit != 0:
            remain_bit = subnet_bit_data.get(inactive_bit)
            default_bit[current_index] = remain_bit

        self.__subnet_bit = f"{default_bit[0]}.{default_bit[1]}.{default_bit[2]}.{default_bit[3]}"
        self.__subnet = input_subnet

    def full_range(self):
        self.networkAddress = self.ip.split('.')
        subnet_bit_break = self.__subnet_bit.split('.')
        convert = 0
        for index, subnet_bit in enumerate(subnet_bit_break):
            if int(subnet_bit) != int(255):
                convert = int(self.networkAddress[index]) & int(subnet_bit)
                self.networkAddress[index] = str(convert)

        for index, bit in enumerate(subnet_bit_break):
            current_bit = int(bit)

            if current_bit != 255 and current_bit != 0:
                subnet_bit_break[index] = str(255 - current_bit)

            if current_bit == 0:
                subnet_bit_break[index] = "255"
            
            if current_bit == 255:
                subnet_bit_break[index] = self.networkAddress[index]


        self.networkAddress = f"{self.networkAddress[0]}.{self.networkAddress[1]}.{self.networkAddress[2]}.{self.networkAddress[3]}"
        mixed_subnet_bit_break = f"{subnet_bit_break[0]}.{subnet_bit_break[1]}.{subnet_bit_break[2]}.{subnet_bit_break[3]}"
        self.__ip_broadcast = mixed_subnet_bit_break
        self.__ip_full_range = f"{self.networkAddress} - {mixed_subnet_bit_break}"
        return self.__ip_full_range
    
    def usable_range(self):
        self.networkAddress = self.ip.split('.')
        subnet_bit_break = self.__subnet_bit.split('.')
        convert = 0
        for index, subnet_bit in enumerate(subnet_bit_break):
            if int(subnet_bit) != int(255):
                convert = int(self.networkAddress[index]) & int(subnet_bit)
                self.networkAddress[index] = str(convert)

        for index, bit in enumerate(subnet_bit_break):
            current_bit = int(bit)

            if current_bit != 255 and current_bit != 0:
                subnet_bit_break[index] = str(255 - current_bit)

            if current_bit == 0:
                subnet_bit_break[index] = "255"
            
            if current_bit == 255:
                subnet_bit_break[index] = self.networkAddress[index]
        convert1 = int(self.networkAddress[3]) + 1
        convert2 = int(subnet_bit_break[3]) + 1
        self.networkAddress[3] = str(convert1)
        subnet_bit_break[3] = str(convert2)

        self.networkAddress = f"{self.networkAddress[0]}.{self.networkAddress[1]}.{self.networkAddress[2]}.{self.networkAddress[3]}"
        mixed_subnet_bit_break = f"{subnet_bit_break[0]}.{subnet_bit_break[1]}.{subnet_bit_break[2]}.{subnet_bit_break[3]}"
        self.__ip_broadcast = mixed_subnet_bit_break
        self.__ip_full_range = f"{self.networkAddress} - {mixed_subnet_bit_break}"
        return self.__ip_full_range

    def info(self):
        if self.__subnet == None:
            print(f"Ip address      : {self.ip}")
            print(f"Ip class        : {self.__ip_class}")

        else:
            print(f"Ip address      : {self.ip}")
            print(f"Ip class        : {self.__ip_class}\n")
            print(f"Subnet Bit({self.__subnet}) : {self.__subnet_bit}")
            print(f"Full range      : {self.full_range()}")
            print(f"Ip host         : {self.networkAddress}")
            print(f"Ip broadcast    : {self.__ip_broadcast}")
            print(f"Usable range    : {self.usable_range()}")
