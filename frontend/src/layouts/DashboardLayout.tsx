import * as React from "react"
import { Outlet } from "react-router-dom"
import { Sidebar } from "../components/Sidebar"
import { Bell, Search, UserCircle } from "lucide-react"

export function DashboardLayout() {
  // Mock role for now, in a real app this comes from Auth Context
  const [role] = React.useState<"admin" | "lecturer" | "student">("lecturer")

  return (
    <div className="flex h-screen w-full bg-background overflow-hidden">
      <Sidebar role={role} />
      
      <div className="flex flex-1 flex-col overflow-hidden">
        {/* Top App Bar */}
        <header className="flex h-16 items-center justify-between border-b bg-card px-6 shadow-sm">
          <div className="flex items-center gap-4 bg-muted px-3 py-1.5 rounded-md w-64 border border-input focus-within:ring-2 focus-within:ring-ring focus-within:border-transparent">
            <Search size={18} className="text-muted-foreground" />
            <input 
              type="text" 
              placeholder="Search..." 
              className="bg-transparent text-sm focus:outline-none w-full text-foreground"
            />
          </div>
          
          <div className="flex items-center gap-4">
            <button className="relative text-muted-foreground hover:text-foreground transition-colors">
              <Bell size={20} />
              <span className="absolute top-0 right-0 h-2 w-2 rounded-full bg-destructive"></span>
            </button>
            <div className="h-8 w-px bg-border"></div>
            <div className="flex items-center gap-2 cursor-pointer">
              <div className="flex flex-col items-end text-sm">
                <span className="font-medium leading-none">Jane Doe</span>
                <span className="text-xs text-muted-foreground mt-1 capitalize">{role}</span>
              </div>
              <UserCircle size={32} className="text-primary" />
            </div>
          </div>
        </header>

        {/* Main Content Area */}
        <main className="flex-1 overflow-auto bg-muted/20 p-8">
          <div className="mx-auto max-w-6xl">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  )
}
