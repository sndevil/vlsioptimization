module V3 (c , V#1# , V#2# , V#3#); 
input c , V#1# , V#2#;
output V#3#;
wire W#0#0# , W#1#;

not f0 (W#2#0# , c);
xor f1 (W#2#1# , V#1# , V#2#);
and f2 (V#3# , W#2#1# , W#2#0#);
endmodule