function varargout = digitally_synthesized_step_ramp_function(varargin)
% DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION MATLAB code for digitally_synthesized_step_ramp_function.fig
%      DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION, by itself, creates a new DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION or raises the existing
%      singleton*.
%
%      H = DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION returns the handle to a new DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION or the handle to
%      the existing singleton*.
%
%      DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION.M with the given input arguments.
%
%      DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION('Property','Value',...) creates a new DIGITALLY_SYNTHESIZED_STEP_RAMP_FUNCTION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before digitally_synthesized_step_ramp_function_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to digitally_synthesized_step_ramp_function_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help digitally_synthesized_step_ramp_function

% Last Modified by GUIDE v2.5 12-Mar-2015 11:53:23

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @digitally_synthesized_step_ramp_function_OpeningFcn, ...
                   'gui_OutputFcn',  @digitally_synthesized_step_ramp_function_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before digitally_synthesized_step_ramp_function is made visible.
function digitally_synthesized_step_ramp_function_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to digitally_synthesized_step_ramp_function (see VARARGIN)

% Choose default command line output for digitally_synthesized_step_ramp_function
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes digitally_synthesized_step_ramp_function wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = digitally_synthesized_step_ramp_function_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;



function edit1_Callback(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit1 as text
%        str2double(get(hObject,'String')) returns contents of edit1 as a double


% --- Executes during object creation, after setting all properties.
function edit1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
function pushbutton1_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
