
module F1 ( a, b, c, VV1V );
  input a, b, c;
  output VV1V;
  wire   n3;

  INVX1 U3 ( .A(n3), .Y(VV1V) );
  OAI21XL U4 ( .A0(a), .A1(b), .B0(c), .Y(n3) );
endmodule

