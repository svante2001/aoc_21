let readFile (filename: string): string list =
    let reader = System.IO.File.OpenText filename
    let rec help (r: System.IO.StreamReader) (lst: string list) =
        if not(reader.EndOfStream) then 
            let line = r.ReadLine () 
            help r (line :: lst)
        else lst
    help reader []

let list = (readFile "input.txt")

let rec loop (l: string list) (index: int) (ac: int): int = 
    match l with
        | [] -> ac
        | h :: t when t = [] -> 
            match h.[index] with
                |'0' -> ac
                |_ -> (ac+1)
        | h :: t -> 
            match h.[index] with
                    |'0' -> (loop t index ac)
                    |_ -> (loop t index (ac+1))

let mutable g = []
let mutable e = []
for i = 0 to 11 do
    let a = (loop list i 0)
    if a > 500 then 
        g <- g @ [1]
        e <- e @ [0]
    else 
        g <- g @ [0]
        e <- e @ [1]

printfn "g: %A" g
printfn "e: %A" e
