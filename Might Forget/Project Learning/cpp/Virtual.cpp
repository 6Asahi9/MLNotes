class Operation {
public:
    virtual int apply(int a, int b) = 0;
};

class Add : public Operation {
public:
    int apply(int a, int b) override { return a + b; }
};

class Multiply : public Operation {
public:
    int apply(int a, int b) override { return a * b; }
};

Operation* op = new Multiply();
cout << op->apply(3, 4) << endl;   // 12

op = new Add();
cout << op->apply(3, 4) << endl;   // 7
