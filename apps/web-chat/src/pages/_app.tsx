import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { ChosenUserContextProvider } from "@/modules/user/context/ChosenUserContext";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ChosenUserContextProvider>
      <Component {...pageProps} />
    </ChosenUserContextProvider>
  );
}
