module bcd (
    input [9:0] A,
	 output [6:0] decoder_uni, decoder_dec, decoder_cent, decoder_mil
);

	wire [3:0] mil, cent, dec, uni; 

    assign uni  = A % 10;
    assign dec  = (A / 10) % 10;
    assign cent = (A / 100) % 10;
    assign mil  = A / 1000;

	decoder_7seg DISPLAY_UNI(
	.decoder_in(uni),
	.decoder_out(decoder_uni)
	);
	decoder_7seg DISPLAY_DEC(
	.decoder_in(dec),
	.decoder_out(decoder_dec)
	);
	decoder_7seg DISPLAY_CENT(
	.decoder_in(cent),
	.decoder_out(decoder_cent)
	);
	decoder_7seg DISPLAY_MIL(
	.decoder_in(mil),
	.decoder_out(decoder_mil)
	);
endmodule
