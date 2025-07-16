
`timescale 1ns / 1ps

module tb;

  reg signed [7:0] A = 8'd9;
  reg signed [7:0] B = 8'd8;
  reg [1:0] opcode = 2'b1010;
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
