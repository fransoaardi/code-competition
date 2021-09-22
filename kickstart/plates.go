package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Global struct{
	sumMax int
	sumList [][]int
}

func partialSum(stacks []int) []int{
	ps := make([]int, 0)
	ps = append(ps, 0)
	sum := 0

	for _, val := range stacks{
		sum += val
		ps = append(ps, sum)
	}

	return ps
}

func bt(n, k, sum int, ans []int, g *Global) bool{
	if n == 0 && sum == 0{
		ps := 0
		for idx, v := range ans{
			ps += g.sumList[idx][v]
		}

		if ps > g.sumMax{
			g.sumMax = ps
		}

		return true
	}
	if n == 0{
		return false
	}

	if sum == 0 {
		ps := 0
		for idx, a := range ans{
			ps += g.sumList[idx][a]
		}

		if ps > g.sumMax{
			g.sumMax = ps
		}

		return false
	}

	for i:= k; i>=0; i--{
		if sum - i >= 0{
			bt(n-1, k, sum-i, append(ans, i), g)
		}
	}

	return true
}

func main(){
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())

	for i:= 0; i<t; i++{
		scanner.Scan()
		read := scanner.Text()

		nkp := strings.Split(read, " ")
		n, _ := strconv.Atoi(nkp[0])
		k, _ := strconv.Atoi(nkp[1])
		p, _ := strconv.Atoi(nkp[2])

		stacks := make([][]int, n)

		for j:=0; j<n; j++{
			scanner.Scan()
			stVal := strings.Split(scanner.Text(), " ")
			tmp := make([]int, k)
			for idx, v := range stVal{
				tmp[idx], _ = strconv.Atoi(v)
			}
			stacks[j] = partialSum(tmp)
		}

		g := new(Global)
		g.sumMax = -1
		g.sumList = stacks
		bt(n, k, p, make([]int,0), g)
		fmt.Printf("Case #%v: %v\n", i, g.sumMax)
	}

}
