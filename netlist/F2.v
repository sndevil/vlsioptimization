
module F2 ( VV1V, c, VV2V );
  input VV1V, c;
  output VV2V;


  XOR2X1 U2 ( .A(c), .B(VV1V), .Y(VV2V) );
endmodule

