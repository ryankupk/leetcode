func destCity(paths [][]string) string {
    dest := paths[0][1]
    for {
        dummy := dest
        for _, path := range paths[1:] {
            if path[0] == dest {
                dest = path[1]
            }
        }
        if dummy == dest {
            return dest
        }
    }
}
