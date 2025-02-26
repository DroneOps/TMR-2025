module decoder_7seg (
  input [3:0] decoder_in,   
  output reg [6:0] decoder_out  
);

  always @(*) 
  begin
    case (decoder_in) 
      4'b0000: decoder_out = 7'b0000001; 
	4'b0001: decoder_out = 7'b1001111;  
	4'b0010: decoder_out = 7'b0010010;  
	4'b0011: decoder_out = 7'b0000110; 
	4'b0100: decoder_out = 7'b1001100;  
	4'b0101: decoder_out = 7'b0100100;  
	4'b0110: decoder_out = 7'b0100000;  
	4'b0111: decoder_out = 7'b0001111;   
	4'b1000: decoder_out = 7'b0000000;  
	4'b1001: decoder_out = 7'b0000100;    
	default: decoder_out = 7'b1111111;  
    endcase
  end
endmodule
 