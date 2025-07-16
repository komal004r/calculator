# calculator

# Verilog ALU Simulation with Python-Driven 7-Segment Display

This project implements an **Arithmetic Logic Unit (ALU)** in Verilog and automates its testing using a **Python script**. It simulates output display on a **7-segment LED** by printing the result visually in the terminal. The setup mimics an FPGA development workflow, though all execution is done in simulation using Icarus Verilog.

---

## 🚀 Features

- ✅ Verilog-based ALU supporting addition, subtraction, multiplication, and scaled integer division  
- ✅ Dynamic input handling using Python (`input.txt` as source)  
- ✅ Automated testbench (`tb.v`) generation with simulation via Icarus Verilog  
- ✅ Visual 7-segment LED output rendered in ASCII using Python  
- ✅ Modular code structure with potential for FPGA deployment

---

## 📁 Files Included

| File              | Description                                      |
|-------------------|--------------------------------------------------|
| `alu.v`           | Verilog ALU module with 4 arithmetic operations  |
| `display_driver.v`| Converts numeric result into 7-segment codes     |
| `tb.v`            | Dynamically generated testbench (via Python)     |
| `python.py`       | Main Python script to handle automation and display |
| `input.txt`       | Input values: `A B opcode`                       |
| `output.txt`      | Simulation output (including ALU result & segs)  |

---

## 📝 Input Format

You provide inputs via the `input.txt` file. Example:

```

9 8 10

````

This means:
- A = 9
- B = 8
- Opcode = `10` (Multilplication)

**Supported Opcodes:**

| Opcode | Operation     |
|--------|---------------|
| `00`   | Addition       |
| `01`   | Subtraction    |
| `10`   | Multiplication |
| `11`   | Division (scaled to 2 decimal places) |

---

## ⚙️ How to Run

1. Install **Icarus Verilog** if not already installed:  
   - Windows (via Chocolatey): `choco install icarus-verilog`
   - Linux: `sudo apt install iverilog`

2. In your terminal or VS Code:

```bash
python python.py
````

3. Output appears in:

   * Terminal as numeric result
   * Terminal as visual **7-segment display**

---

## 🔍 Sample Output

### `input.txt`

```
9 8 10
```

### Terminal Output:

```
Result from ALU (Multiplication): 072

7-Segment Display:

<img width="648" height="251" alt="Screenshot 2025-07-16 152216" src="https://github.com/user-attachments/assets/2642ea87-955b-4725-bf84-7a3180eb4e0f" />



## 💡 Future Enhancements

* Add support for negative numbers and decimal points on display
* Export waveform using `.vcd` for GTKWave analysis
* Port to real FPGA board using open-source toolchains (Yosys, nextpnr)
* Add GUI or web interface for user input

## 👩‍💻 Author

**Komal Sharma**
B.Tech, Electronics and IoT
GitHub: \[komal004r]


## 📜 License

This project is open source and free to use for learning and academic purposes.

