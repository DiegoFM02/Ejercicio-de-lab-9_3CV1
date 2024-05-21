#Para valores distintos
def magic_index_distinct(arr):
    def magic_index_helper(arr, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if arr[mid] == mid:
            return mid
        elif arr[mid] > mid:
            return magic_index_helper(arr, start, mid - 1)
        else:
            return magic_index_helper(arr, mid + 1, end)
    
    return magic_index_helper(arr, 0, len(arr) - 1)

# Ejemplo de uso
if __name__ == "__main__":
    arr = [-10, -5, 0, 3, 7, 9, 12]
    print("Índice mágico:", magic_index_distinct(arr))  # Debería imprimir: Índice mágico: 3



#Para valores no distintos
def magic_index_non_distinct(arr):
    def magic_index_helper(arr, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if arr[mid] == mid:
            return mid
        
        # Buscar en la mitad izquierda
        left_index = min(mid - 1, arr[mid])
        left = magic_index_helper(arr, start, left_index)
        if left >= 0:
            return left
        
        # Buscar en la mitad derecha
        right_index = max(mid + 1, arr[mid])
        right = magic_index_helper(arr, right_index, end)
        return right
    
    return magic_index_helper(arr, 0, len(arr) - 1)

# Ejemplo de uso
if __name__ == "__main__":
    arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12]
    print("Índice mágico:", magic_index_non_distinct(arr))  # Debería imprimir: Índice mágico: 2
