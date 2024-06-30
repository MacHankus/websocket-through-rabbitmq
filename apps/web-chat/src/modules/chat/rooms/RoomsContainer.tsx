"use client";

import React from "react";
import useSWR, { Fetcher } from "swr";
import { ChosenUserContext } from "../../user/context/ChosenUserContext";


export const RoomsContainer = () => {
  const { user, setUser } = React.useContext(ChosenUserContext);

  const { data } = useSWR(uid, fetcher)
};


