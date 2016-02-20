
module F4 ( VV2V, p, v, VV3V, VV4V );
  input VV2V, p, v, VV3V;
  output VV4V;
  wire   n2;

  NOR2BX1 U3 ( .AN(VV3V), .B(n2), .Y(VV4V) );
  NOR3X1 U4 ( .A(VV2V), .B(v), .C(p), .Y(n2) );
endmodule

