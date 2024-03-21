class HanoiTower:
    def move(self, n, source, target, auxiliary):
        if n == 1:
            print(f"Di chuyển đĩa từ tháp {source} sang tháp {target}")
            return
        self.move(n - 1, source, auxiliary, target)
        print(f"Di chuyển đĩa từ tháp {source} sang tháp {target}")
        self.move(n - 1, auxiliary, target, source)

# Khởi tạo đối tượng HanoiTower
hanoi_tower = HanoiTower()

# Di chuyển tháp Hanoi có 3 tầng từ vị trí 1 đến vị trí 3 thông qua vị trí trung gian 2
hanoi_tower.move(3, 1, 3, 2)
