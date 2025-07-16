import os

# Step 1: Read A, B, and opcode from input.txt
with open("input.txt", "r") as f:
    parts = f.read().strip().split()
    A, B, opcode = int(parts[0]), int(parts[1]), int(parts[2])

# Step 2: Generate dynamic testbench
testbench = f"""
`timescale 1ns / 1ps

module tb;

  reg signed [7:0] A = 8'd{A};
  reg signed [7:0] B = 8'd{B};
  reg [1:0] opcode = 2'b{opcode:02b};
  wire signed [15:0] result;
  wire [6:0] seg_hundreds, seg_tens, seg_ones;

  alu uut(.A(A), .B(B), .opcode(opcode), .result(result));

  display_driver disp (
    .result(result),
    .seg_hundreds(seg_hundreds),
    .seg_tens(seg_tens),
    .seg_ones(seg_ones)
  );

  initial begin
    #10;
    $display("Result from ALU: %d", result);
    $display("SEGS: %b %b %b", seg_hundreds, seg_tens, seg_ones);
    $finish;
  end

endmodule
"""

# Step 3: Write testbench to file
with open("tb.v", "w") as f:
    f.write(testbench)

# Step 4: Compile and simulate
print("Compiling...")
compile_status = os.system("iverilog -o sim alu.v display_driver.v tb.v")
if compile_status != 0:
    print("❌ Compilation failed!")
else:
    print("Simulation running...")
    sim_status = os.system("vvp sim > output.txt 2>&1")
    if sim_status != 0:
        print("❌ Simulation failed!")
    else:
        print("✅ Simulation done.")

# Step 5: Show output
with open("output.txt", "r") as f:
    lines = f.readlines()

result_line = ""
seg_data = None

for line in lines:
    if "Result from ALU" in line:
        result_line = line.strip()
    if "SEGS:" in line:
        seg_data = line.replace("SEGS:", "").strip()

if result_line:
    if opcode == 3:
        val = int(result_line.split()[-1])
        print(f"Result from ALU (Division): {val / 100.0:.2f}")
    else:
        print(result_line)
else:
    print("[No ALU result found]")

# Render 7-segment display
SEGMENTS = {
    '1000000': [" _ ", "| |", "|_|"],  # 0
    '1111001': ["   ", "  |", "  |"],  # 1
    '0100100': [" _ ", " _|", "|_ "],  # 2
    '0110000': [" _ ", " _|", " _|"],  # 3
    '0011001': ["   ", "|_|", "  |"],  # 4
    '0010010': [" _ ", "|_ ", " _|"],  # 5
    '0000010': [" _ ", "|_ ", "|_|"],  # 6
    '1111000': [" _ ", "  |", "  |"],  # 7
    '0000000': [" _ ", "|_|", "|_|"],  # 8
    '0010000': [" _ ", "|_|", "  |"],  # 9
    '1111111': ["   ", "   ", "   "]   # blank
}

def render_seven_segment(binary_segments):
    digits = binary_segments.strip().split()
    lines = ["", "", ""]
    for seg in digits:
        seg_repr = SEGMENTS.get(seg, ["???", "???", "???"])
        for i in range(3):
            lines[i] += seg_repr[i] + " "
    print("\n".join(lines)) 


if seg_data is None:
    print("❌ Error: No 'SEGS:' line found in output.txt")
else:
    print("\n7-Segment Display:\n")
    print(render_seven_segment(seg_data))
