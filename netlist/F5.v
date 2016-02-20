
module F4 ( VV2V, VV3V, VV4V );
  input VV2V, VV3V;
  output VV4V;


  AND2X1 U3 ( .A(VV3V), .B(VV2V), .Y(VV4V) );
endmodule

