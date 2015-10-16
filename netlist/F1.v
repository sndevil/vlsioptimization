
module F1 ( a, b, VV1V );
  input a, b;
  output VV1V;


  OR2X1 U2 ( .A(a), .B(b), .Y(VV1V) );
endmodule

