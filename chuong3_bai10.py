class DaThuc:
    # Code của phần khai báo __init__ và các phương thức khác không thay đổi

    def DoiDau(self):
        current = self.head
        while current:
            current.heso = -current.heso
            current = current.next
