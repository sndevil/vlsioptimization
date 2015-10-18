module F266 (VV250V , VV265V , VV266V); 
input VV250V , VV265V;
output VV266V;
or f0 (VV266V , VV250V , VV265V);
endmodule