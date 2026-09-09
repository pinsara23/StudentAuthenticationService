import * as React from "react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../components/ui/Card"
import { Button } from "../components/ui/Button"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "../components/ui/Table"
import { Input } from "../components/ui/Input"
import { Search, Save, CheckCircle2, XCircle, Clock, Users } from "lucide-react"

// Mock Data
const MOCK_STUDENTS = [
  { id: "S101", name: "Alice Johnson", email: "alice@example.com" },
  { id: "S102", name: "Bob Smith", email: "bob@example.com" },
  { id: "S103", name: "Charlie Davis", email: "charlie@example.com" },
  { id: "S104", name: "Diana Prince", email: "diana@example.com" },
  { id: "S105", name: "Evan Wright", email: "evan@example.com" },
]

type AttendanceStatus = "present" | "absent" | "late" | null

export function AttendanceMarking() {
  const [attendance, setAttendance] = React.useState<Record<string, AttendanceStatus>>({})
  const [searchQuery, setSearchQuery] = React.useState("")

  const handleMark = (studentId: string, status: AttendanceStatus) => {
    setAttendance((prev) => ({
      ...prev,
      [studentId]: prev[studentId] === status ? null : status, // Toggle off if clicked again
    }))
  }

  const markAllPresent = () => {
    const newAttendance: Record<string, AttendanceStatus> = {}
    MOCK_STUDENTS.forEach((s) => {
      newAttendance[s.id] = "present"
    })
    setAttendance(newAttendance)
  }

  const filteredStudents = MOCK_STUDENTS.filter(
    (s) =>
      s.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      s.id.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const presentCount = Object.values(attendance).filter((s) => s === "present").length
  const absentCount = Object.values(attendance).filter((s) => s === "absent").length
  const lateCount = Object.values(attendance).filter((s) => s === "late").length

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold tracking-tight">Mark Attendance</h1>
        <p className="text-muted-foreground mt-1">Session: Advanced Computer Networks (CS-401) - Today, 10:00 AM</p>
      </div>

      <div className="grid gap-6 md:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Total Students</CardTitle>
            <Users className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{MOCK_STUDENTS.length}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-green-600">Present</CardTitle>
            <CheckCircle2 className="h-4 w-4 text-green-600" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-green-600">{presentCount}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-red-600">Absent</CardTitle>
            <XCircle className="h-4 w-4 text-red-600" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-red-600">{absentCount}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium text-orange-500">Late</CardTitle>
            <Clock className="h-4 w-4 text-orange-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-orange-500">{lateCount}</div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Student List</CardTitle>
              <CardDescription>Select student status to mark attendance for this session.</CardDescription>
            </div>
            <div className="flex gap-4">
              <Button variant="outline" onClick={markAllPresent}>Mark All Present</Button>
              <Button className="gap-2">
                <Save size={16} /> Save Attendance
              </Button>
            </div>
          </div>
          <div className="mt-4 flex max-w-sm items-center gap-2">
            <div className="relative w-full">
              <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
              <Input
                type="text"
                placeholder="Search students..."
                className="pl-9"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>
          </div>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead className="w-[100px]">ID</TableHead>
                <TableHead>Name</TableHead>
                <TableHead>Email</TableHead>
                <TableHead className="text-right">Action</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredStudents.map((student) => (
                <TableRow key={student.id}>
                  <TableCell className="font-medium">{student.id}</TableCell>
                  <TableCell>{student.name}</TableCell>
                  <TableCell>{student.email}</TableCell>
                  <TableCell className="text-right">
                    <div className="flex justify-end gap-2">
                      <Button
                        size="sm"
                        variant={attendance[student.id] === "present" ? "default" : "outline"}
                        className={attendance[student.id] === "present" ? "bg-green-600 hover:bg-green-700 text-white" : ""}
                        onClick={() => handleMark(student.id, "present")}
                      >
                        Present
                      </Button>
                      <Button
                        size="sm"
                        variant={attendance[student.id] === "absent" ? "default" : "outline"}
                        className={attendance[student.id] === "absent" ? "bg-red-600 hover:bg-red-700 text-white" : ""}
                        onClick={() => handleMark(student.id, "absent")}
                      >
                        Absent
                      </Button>
                      <Button
                        size="sm"
                        variant={attendance[student.id] === "late" ? "default" : "outline"}
                        className={attendance[student.id] === "late" ? "bg-orange-500 hover:bg-orange-600 text-white" : ""}
                        onClick={() => handleMark(student.id, "late")}
                      >
                        Late
                      </Button>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
              {filteredStudents.length === 0 && (
                <TableRow>
                  <TableCell colSpan={4} className="text-center py-6 text-muted-foreground">
                    No students found matching your search.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  )
}
