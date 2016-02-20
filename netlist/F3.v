
module F3 ( d, a, c, VV3V );
  input d, a, c;
  output VV3V;
  wire   n2;

  XOR2X1 U3 ( .A(d), .B(n2), .Y(VV3V) );
  NOR2X1 U4 ( .A(a), .B(c), .Y(n2) );
endmodule

