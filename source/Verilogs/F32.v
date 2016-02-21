module F32 (c , a , VV32V); 
input c , a;
output VV32V;
wire WW31W0W , WW31W1W;

not f0 (WW31W0W , c);
not f1 (WW31W1W , a);
or f2 (VV32V , WW31W0W , WW31W1W);
endmodule