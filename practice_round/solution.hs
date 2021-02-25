import Data.List
import qualified Data.Set as S

type Ingredient = String
data Pizzas = Pizzas 
    { labels :: [Int]
    , ingredients :: (S.Set Ingredient)
    }

instance Show Pizzas where
    show (Pizzas ns _) = "Pizzas " ++ show ns

parsePizzas :: String -> [Pizzas]
parsePizzas = zipWith Pizzas (map (:[]) [0..]) . map (S.fromList . tail . words) . tail . lines

parseTeams :: String -> [Int]
parseTeams = map read . tail . words . head . lines

overlap :: Pizzas -> Pizzas -> Int
overlap (Pizzas _ l) (Pizzas _ r) = S.size $ S.intersection l r

merge :: Pizzas -> Pizzas -> Pizzas
merge (Pizzas ns ings) (Pizzas ns' ings') = Pizzas (ns ++ ns') (S.union ings ings')

reduce :: Int -> [Pizzas] -> [Pizzas]
reduce t [] = []
reduce t (p@(Pizzas [_,_,_,_] _):ps) = p : reduce t ps
reduce t (p:ps) = case partition ((< t) . overlap p) ps of
    ([], _)          -> p : reduce t ps
    ((p':ps'), ps'') -> reduce t $ merge p p' : ps' ++ ps''

solve :: Int -> String -> String
solve t input =
    let nss = map labels $ reduce t $ parsePizzas input
        [l2, l3, l4] = parseTeams input
        (nss4'', nss4''') = partition ((>= 4) . length) nss
        (nss4, nss4') = splitAt l4 nss4''
        (nss3'', nss3''') = partition ((>= 3) . length) $ nss4' ++ nss4'''
        (nss3, nss3') = splitAt l3 $ map (take 3) nss3''
        (nss2'', nss2''') = partition ((>= 2) . length) $ nss3' ++ nss3'''
        (nss2, nss2') = splitAt l2 $ map (take 2) nss2''
        matrix = [length (nss2 ++ nss3 ++ nss4)] : map (2:) nss2 ++ map (3:) nss3 ++ map (4:) nss4
    in  unlines $ map (unwords . map show) matrix

main :: IO ()
main = do
    writeFile "output_A" =<< solve 2 <$> readFile "input_A"
    writeFile "output_B" =<< solve 1 <$> readFile "input_B"
    writeFile "output_C" =<< solve 1 <$> readFile "input_C"
    writeFile "output_D" =<< solve 1 <$> readFile "input_D"
    writeFile "output_E" =<< solve 1 <$> readFile "input_E"
