let reader = System.IO.File.OpenText "input.txt"
let lines = reader.ReadLine().Split (",")
let lst = lines |> Array.toList |> List.map (fun x -> int x)
let max = lst |> List.max

let mutable fuelList = []
for i = 0 to max do 
    let mutable fuel = 0
    for j = 0 to lst.Length-1 do
        let n = (abs (lst.[j] - i))
        fuel <- fuel + (((n-1) * (n)) / 2) + n
    fuelList <- fuelList @ [fuel]

printfn "%A" (fuelList |> List.min)