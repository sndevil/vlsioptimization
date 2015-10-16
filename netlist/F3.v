
module F3 ( a, c, VV3V );
  input a, c;
  output VV3V;


  XOR2X1 U2 ( .A(c), .B(a), .Y(VV3V) );
endmodule

