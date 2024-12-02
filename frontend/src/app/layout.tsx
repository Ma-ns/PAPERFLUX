import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Sidebar from "@/components/common/Sidebar";

const inter = localFont({
  src: "./fonts/Inter.ttf",
  variable: "--font-inter",
  weight: "100 200 300 400 500 600 700 800 900",
});

export const metadata: Metadata = {
  title: "Paperflux"
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-br">
      <body
        className={`${inter.variable} font-inter antialiased flex text-slate-950`}
      >
        <nav className="h-[100vh] w-[25%]">
          <Sidebar />
        </nav>
        <main className="h-[100vh] w-full bg-slate-50 flex items-center justify-center py-9 px-8 overflow-hidden">
          {children}
        </main>
      </body>
    </html>
  );
}
