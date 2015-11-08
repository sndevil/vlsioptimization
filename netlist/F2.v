
module F2 ( a, VV1V, VV2V );
  input a, VV1V;
  output VV2V;


  XNOR2X1 U2 ( .A(a), .B(VV1V), .Y(VV2V) );
endmodule

