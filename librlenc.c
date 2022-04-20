#include <stdio.h>
#include <limits.h>

typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
/* typedef unsigned int uint32_t; */

typedef uint8_t arr_t;
typedef unsigned long arr_size_t;
typedef uint16_t buffer_t;      // To store encoded outcome
#define MAX_BUFFER_VAL USHRT_MAX

// Return buffer length or -1 for not enough buffer
long encode_simple(arr_t * arr, arr_size_t arr_size, buffer_t * buffer, arr_size_t buffer_len){
    long counter = 0;
    buffer_t sum_len = 1;
    arr_t prev_elem = arr[0];

    for (int i = 0; i< arr_size; i++){
        if (i!=arr_size-1 && arr[i+1] == arr[i] && sum_len < MAX_BUFFER_VAL){
            sum_len += 1;
        }
        else{
            // record
            if (counter + 1 > buffer_len-1){
                return -1;
            }
            buffer[counter] = sum_len;
            buffer[counter + 1] = prev_elem;
            counter += 2;
            sum_len = 1;
            if (i!=arr_size -1){
                prev_elem = arr[i+1];
            }
        }
    }
    return counter;
}

// return array size or -1 for not enough buffer
long decode_simple(buffer_t * encoded, arr_size_t encoded_size, arr_t * arr_buffer, arr_size_t arr_size){
    long counter = 0;
    buffer_t _len;
    arr_t _val;

    long i = 0;
    while(i < encoded_size){
        _len = encoded[i];
        _val = (arr_t)encoded[i+1];
        i += 2;

        if(counter+_len > arr_size){
            return -1;
        }

        for (long j = counter; j< counter + _len; j++){
            arr_buffer[j] = _val;
        }
        counter += _len;
    }
    return counter;
}

int main(){
    return 0;
}
