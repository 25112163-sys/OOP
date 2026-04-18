#include <iostream>
#include <cmath>
using namespace std;

class Point {
private:
    double x, y;

public:
    // Constructor
    Point(double a = 0, double b = 0) {
        x = a;
        y = b;
    }

    // Nhập tọa độ
    void input() {
        cout << "Nhap x: ";
        cin >> x;
        cout << "Nhap y: ";
        cin >> y;
    }

    // Hiển thị tọa độ
    void display() {
        cout << "(" << x << ", " << y << ")" << endl;
    }

    // Lấy giá trị x và y
    double getX() { return x; }
    double getY() { return y; }

    // Điểm đối xứng qua gốc O
    Point symmetric() {
        return Point(-x, -y);
    }

    // Khoảng cách đến gốc O
    double distanceToO() {
        return sqrt(x*x + y*y);
    }

    // Khoảng cách giữa hai điểm
    double distanceTo(Point p) {
        return sqrt(pow(x - p.x, 2) + pow(y - p.y, 2));
    }
};

int main() {
    // 1. Tạo điểm A(3,4)
    Point A(3,4);
    cout << "Diem A: ";
    A.display();

    // 2. Nhập điểm B
    Point B;
    cout << "Nhap diem B:\n";
    B.input();

    cout << "Diem B: ";
    B.display();

    // 3. Điểm C đối xứng của B qua O
    Point C = B.symmetric();
    cout << "Diem C doi xung cua B qua O: ";
    C.display();

    // 4. Khoảng cách từ B đến O
    cout << "Khoang cach tu B den O: " << B.distanceToO() << endl;

    // 5. Khoảng cách từ A đến B
    cout << "Khoang cach tu A den B: " << A.distanceTo(B) << endl;

    // 6. Khoảng cách từ C đến O
    cout << "Khoang cach tu C den O: " << C.distanceToO() << endl;

    return 0;
}