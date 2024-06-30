import { Paper, Grid, TextField, Typography, Button } from "@mui/material";
import { useContext } from "react";
import { useState } from "react";
import { ChosenUserContext } from "./context/ChosenUserContext";
import { useRouter } from 'next/navigation'
import { styled } from "@mui/system";
import Link from "next/link";

const LoginBox = styled(Paper)(({ theme }) => ({
  width: "100%",
  height: "100%",
  padding: "20px",
  [theme.breakpoints.up("sm")]: {
    width: "300px",
    height: "200px",
  },
}));

export const ChooseUserForm = () => {
  const { user, setUser } = useContext(ChosenUserContext);
  const [providedUser, setProvidedUser] = useState<string>("");
  const router = useRouter()
  return (
    <Grid
      container
      width={"100%"}
      height={"100%"}
      justifyContent={"center"}
      alignContent={"center"}
    >
      <LoginBox>
        <form
          onSubmit={(e: React.FormEvent) => {
            e.preventDefault();
            console.log("settings username");
            console.log(providedUser);
            setUser({ username: providedUser });
            router.push("/chat");
          }}
        >
          <Grid
            container
            width={"100%"}
            height={"100%"}
            justifyContent={"flex-start"}
            direction={"column"}
            spacing={2}
          >
            <Grid item>
              <Typography fontSize={"13px"}>Type your name to join</Typography>
            </Grid>
            <Grid item>
              <TextField
                id={"Username"}
                label={"Username"}
                size={"small"}
                onChange={(value: React.ChangeEvent<HTMLInputElement>) => {
                  setProvidedUser(value.target.value);
                }}
              ></TextField>
            </Grid>
            <Grid item>
              <Button type="submit" variant="contained">
                Submit
              </Button>
            </Grid>
            <Grid item alignSelf={"end"}>
              {user !== undefined && (
                <Typography color={"blue"}>
                  <Link href="/chat">or continue as {user.username}</Link>
                </Typography>
              )}
            </Grid>
          </Grid>
        </form>
      </LoginBox>
    </Grid>
  );
};
