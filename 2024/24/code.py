# AoC Day 24
# @author: Friedrich Leez

def apply_gate(op, input1, input2=None):
    """Apply a boolean operation based on the type of the gate."""
    if op == "AND":
        return input1 & input2
    elif op == "OR":
        return input1 | input2
    elif op == "XOR":
        return input1 ^ input2
    else:
        raise ValueError(f"Unsupported gate operation: {op}")


def parse_input(file_path):
    """Parse the input file to extract wire values and gate operations."""
    wire_values = {}
    gates = []

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if not line:  # Skip empty lines
                continue

            if "->" in line:
                # This line represents a gate operation
                parts = line.split(" -> ")
                gate_expr = parts[0]
                output_wire = parts[1]
                gates.append((gate_expr, output_wire))
                print(f"Gate: {gate_expr} -> {output_wire}")  # Debugging line
            else:
                # This line represents an initial wire value
                if ": " in line:
                    wire, value = line.split(": ")
                    wire_values[wire] = int(value)
                else:
                    print(f"Warning: Skipping malformed line: {line}")

    return wire_values, gates


def evaluate_wire(wire_values, gates, wire):
    """Evaluate the value of a wire by processing all gates."""
    if wire in wire_values:
        return wire_values[wire]

    # Evaluate all gates until we find the correct one for this wire
    for gate_expr, output_wire in gates:
        if output_wire == wire:
            # If the wire is the output of this gate, process the gate's expression
            if "AND" in gate_expr:
                inputs = gate_expr.split(" AND ")
                op = "AND"
            elif "OR" in gate_expr:
                inputs = gate_expr.split(" OR ")
                op = "OR"
            elif "XOR" in gate_expr:
                inputs = gate_expr.split(" XOR ")
                op = "XOR"
            else:
                raise ValueError(f"Unsupported gate operation in expression: {gate_expr}")

            # Evaluate the input wires before applying the operation
            input_values = [evaluate_wire(wire_values, gates, inp) for inp in inputs]

            # Apply the operation (AND, OR, XOR)
            if len(input_values) == 1:
                result = ~input_values[0] & 0xFFFF  # For NOT operation, assuming 16-bit limits
            else:
                result = apply_gate(op, *input_values)

            # Store the result and return it
            wire_values[wire] = result
            print(f"Evaluating wire {wire}: {result}")  # Debugging line
            return result

    # If no evaluation was found for the wire, raise an error
    raise ValueError(f"Wire {wire} not found or evaluated")



def get_z_value(wire_values, gates):
    """Get the value of the first wire starting with 'z'."""
    z_wires = [wire for wire in wire_values if wire.startswith('z')]
    if not z_wires:
        print("No wires starting with 'z' found")
    else:
        print(f"Evaluating wires starting with 'z': {z_wires}")

    for z_wire in z_wires:
        result = evaluate_wire(wire_values, gates, z_wire)
        print(f"Final value for {z_wire}: {result}")
        return result

    raise ValueError("No wires starting with 'z' were found or evaluated.")



def main(file_path):
    """Main function to simulate the gates and compute the output."""
    wire_values, gates = parse_input(file_path)

    # Evaluate the values for all wires
    for wire in list(wire_values.keys()):
        evaluate_wire(wire_values, gates, wire)

    # Get the decimal output from the wires starting with 'z'
    result = get_z_value(wire_values, gates)
    print(f"The decimal value output on the wires starting with 'z' is: {result}")


if __name__ == "__main__":
    file_path = "2024/24/file.txt"  # Set the path to your input file
    main(file_path)