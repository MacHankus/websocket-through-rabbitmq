import axios from "axios";
import {roomsUrl} from "./urls";
import useSWR from "swr";
import fetcher from "@/common/api/fetcher";


export function useGetRooms (username: string) {
  const { data, error, isLoading } = useSWR(`/api/rooms`, fetcher)
 
  return {
    user: data,
    isLoading,
    isError: error
  }
}