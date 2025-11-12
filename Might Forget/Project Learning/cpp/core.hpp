#pragma once
#include <Eigen/Dense>

namespace tml {

class Matrix {
private:
    Eigen::MatrixXd data;   // (1)

public:
    // Constructors
    Matrix();                                   // (2)
    Matrix(size_t rows, size_t cols);           // (3)
    Matrix(const Eigen::MatrixXd& mat);         // (4)

    // Access
    double& operator()(size_t i, size_t j);     // (5)
    double operator()(size_t i, size_t j) const;// (6)

    // Operations
    Matrix transpose() const;                   // (7)
    static Matrix identity(size_t n);           // (8)
    void print(const std::string& name = "") const; // (9)

    // Conversion
    Eigen::MatrixXd& raw();                     // (10)
    const Eigen::MatrixXd& raw() const;         // (11)
};

}
