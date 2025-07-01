1. What is the main advantage of using activation functions like ReLU in neural networks?
✅ Correct Answer:
They prevent the vanishing gradient problem

🧠 Why?
ReLU = f(x) = max(0, x)

Unlike sigmoid or tanh, which squash values between 0–1 or –1 to 1, ReLU doesn't compress positive numbers.

This keeps the gradient large enough during backpropagation, especially in deep networks.

⚠️ The vanishing gradient problem happens when:
Gradients become tiny as they pass backward through layers

Early layers learn nothing because they get almost zero signal

ReLU helps by:

Outputting either 0 or a linear, unbounded value (when input is positive)

This avoids "killing" the gradient like sigmoid/tanh often do in deep layers

🚫 Why the other options are wrong:
They prevent overfitting → Nope, that's what dropout or regularization is for

They are linear functions → Also wrong, ReLU is non-linear, which is crucial for neural nets to learn complex patterns
