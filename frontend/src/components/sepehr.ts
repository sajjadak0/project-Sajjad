import type { AlpineTypes } from "../utils/alpine_types";

interface LogTestRefs {
    testakiDiv: HTMLDivElement;
}

interface ILogTest {
    title: string;
    changeTitle: () => void;
    init: (this: AlpineTypes<LogTestRefs> & ILogTest) => void;
}

export function logtest(): ILogTest {
  return {
    title: "first title",
    changeTitle() {
      console.log("title will change ...");
      this.title = "pashmak";
    },
    init() {
        this.$refs.testakiDiv.innerHTML = "Salma kocholo!";
    }
  };
}
