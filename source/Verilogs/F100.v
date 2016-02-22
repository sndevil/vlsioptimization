module F100 (VV96V , VV99V , VV100V); 
input VV96V , VV99V;
output VV100V;
and f0 (VV100V , VV96V , VV99V);
endmodule