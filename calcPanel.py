import wx

operator = ''
num1 = 0

class CalcFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title='Cal',size = (350,375))
        self.SetSizeHints(350,375,350,475)
        self.setup()
        self.Show()

    def setup(self):
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        self.equation_box = wx.TextCtrl(panel,style = wx.TE_RIGHT)
        box.Add(self.equation_box,0,wx.ALL | wx.EXPAND,3)
        self.result_box = wx.TextCtrl(panel,style = wx.TE_RIGHT)
        box.Add(self.result_box,0,wx.ALL | wx.EXPAND,3)
        #By using Gridsizer add buttons
        grid = wx.GridSizer(4,4,8,8)
        buttons = [
                '7', '8', '9', '/',
                '4', '5', '6', '*',
                '1', '2', '3', '-',
                '.', '0', '=', '+',
                ]
        for la in buttons:
            button = wx.Button(panel,label = la)
            grid.Add(button,0,wx.ALL | wx.EXPAND,border = 3)
            button.SetBackgroundColour(wx.Colour(255,230,200,255))
            button.Bind(wx.EVT_BUTTON,self.on_button_press)
        box.Add(grid,proportion = 1,flag =wx.EXPAND,border = 3)

        clearButton = wx.Button(panel,label = 'Clear')
        box.Add(clearButton,0,flag = wx.ALL | wx.EXPAND,border = 1)
        clearButton.Bind(wx.EVT_BUTTON,self.on_button_press)

        panel.SetBackgroundColour(wx.Colour(224,224,224))
        self.equation_box.SetBackgroundColour(wx.Colour(224,224,224))
        self.result_box.SetBackgroundColour(wx.Colour(224,224,224))
        clearButton.SetBackgroundColour(wx.Colour(255,230,200,255))
        panel.SetSizer(box)

    def on_button_press(self,event):
        global operator
        global num1
        label = event.GetEventObject().GetLabel()
        print(f'Button: {label} Press')
        calculation = self.equation_box.GetValue()
        print(f'Get Value: {calculation}')
        if label == '1':
            calculation = calculation + '1'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '2':
            calculation = calculation + '2'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '3':
            calculation = calculation + '3'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '4':
            calculation = calculation + '4'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '5':
            calculation = calculation + '5'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '6':
            calculation = calculation + '6'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '7':
            calculation = calculation + '7'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '8':
            calculation = calculation + '8'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '9':
            calculation = calculation + '9'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '0':
            calculation = calculation + '0'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '.':
            calculation = calculation + '.'
            print(f'Set Value: {calculation}')
            self.equation_box.SetValue(calculation)
        elif label == '+':
            num1 = float(calculation)
            operator = '+'
            calculation = calculation + '+'
            self.equation_box.SetValue(calculation)
        elif label == '-':
            num1 = float(calculation)
            operator = '-'
            calculation = calculation + '-'
            self.equation_box.SetValue(calculation)
        elif label == '*':
            num1 = float(calculation)
            operator = '*'
            calculation = calculation + '*'
            self.equation_box.SetValue(calculation)
        elif label == '/':
            num1 = float(calculation)
            operator = '/'
            calculation = calculation + '/'
            self.equation_box.SetValue(calculation)
        elif label == 'Clear':
            calculation = ' '
            self.equation_box.SetValue(calculation)
            self.result_box.SetValue(calculation)
        
        elif label == '=':
            print(f'1st Number:{num1}')
            val = calculation
            if operator == '+':
                num2 =float((val.split('+')[1]))
                print('Number2:',num2)
                y = num1 + num2
                calculation = str(y)
                print(f'Result from Code : {calculation}')
                self.result_box.SetValue(calculation)
            elif operator == '-':
                num2 =float((val.split('-')[1]))
                print('Number2:',num2)
                y = num1 - num2
                calculation = str(y)
                print(f'Result from Code : {calculation}')
                self.result_box.SetValue(calculation)
            elif operator == '*':
                num2 =float((val.split('*')[1]))
                print('Number2:',num2)
                y = num1 * num2
                calculation = str(y)
                print(f'Result from Code : {calculation}')
                self.result_box.SetValue(calculation)
            elif operator == '/':
                num2 =float((val.split('/')[1]))
                print('Number2:',num2)
                print('Division')
                if num2 == 0:
                    print('ZeroDivisionError Please try again')
                    num2 = ''
                    calculation = ''
                    self.result_box.SetValue(calculation)
                else:
                    y = num1 / num2
                    calculation = str(y)
                    print(f'Result from Code : {calculation}')
                    self.result_box.SetValue(calculation)   

if __name__ == '__main__':
    # Create the application object
    app = wx.App()
    frame = CalcFrame()
    app.MainLoop()