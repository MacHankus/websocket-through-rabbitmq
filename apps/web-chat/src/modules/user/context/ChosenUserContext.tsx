import { createContext, useEffect, useState } from "react";

type ChosenUserContext = {
  user?: ChosenUser | undefined;
  setUser(user: ChosenUser): void;
};

export const ChosenUserContext = createContext<ChosenUserContext>({
  setUser: ()=>{}
});

export const ChosenUserContextProvider = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  const [user, setUser] = useState<ChosenUser | undefined>(undefined);
  const state = { user, setUser };

  useEffect(() => {
    const username = localStorage.getItem("username");
    if (!!username) {
      setUser({ username });
    }
  }, []);

  useEffect(() => {
    if (!!user) {
      localStorage.setItem("username", user.username);
    }
  }, [user]);

  return (
    <ChosenUserContext.Provider value={state}>
      {children}
    </ChosenUserContext.Provider>
  );
};
