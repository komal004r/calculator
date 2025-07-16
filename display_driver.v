module display_driver(
  input signed [15:0] result,
  output [6:0] seg_hundreds,
  output [6:0] seg_tens,
  output [6:0] seg_ones
);

  function [6:0] seven_seg;
    input [3:0] digit;
    begin
      case (digit)
        4'd0: seven_seg = 7'b1000000;
        4'd1: seven_seg = 7'b1111001;
        4'd2: seven_seg = 7'b0100100;
        4'd3: seven_seg = 7'b0110000;
        4'd4: seven_seg = 7'b0011001;
        4'd5: seven_seg = 7'b0010010;
        4'd6: seven_seg = 7'b0000010;
        4'd7: seven_seg = 7'b1111000;
        4'd8: seven_seg = 7'b0000000;
        4'd9: seven_seg = 7'b0010000;
        default: seven_seg = 7'b1111111; // blank
      endcase
    end
  endfunction

  wire [7:0] abs_result;
  wire [3:0] hundreds, tens, ones;

  assign abs_result = (result < 0) ? -result[7:0] : result[7:0];
  assign hundreds = abs_result / 100;
  assign tens     = (abs_result / 10) % 10;
  assign ones     = abs_result % 10;

  assign seg_hundreds = seven_seg(hundreds);
  assign seg_tens     = seven_seg(tens);
  assign seg_ones     = seven_seg(ones);

endmodule
